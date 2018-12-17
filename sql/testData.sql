set @table_schema='unknown_jobs_db';
set @table_name='company';
set @row_count=200;
set @sql=concat('insert into ',@table_schema,'.',@table_name,' select ');
select 
nullif ('please stand by...',
    @sql:=concat(@sql,
        case 
                when data_type='int' then 'round(rand()*2147483647),'
                when data_type='bigint' then 'round(rand()*9223372036854775807),'
                when data_type='smallint' then 'round(rand()*32767),'
                when data_type='tinyint' then 'round(rand()*127 ),'
                when data_type='varchar' then concat('rand_string(',CHARACTER_MAXIMUM_LENGTH,',5),')
                when data_type='date' then 'now()-interval round(90*rand()) day,'
                when data_type='datetime' then 'now()-interval round(90*rand()) day,'
                when data_type='timestamp' then 'now()-interval round(90*rand()) day,'
        end
    )
) info
from information_schema.columns where table_schema=@table_schema and table_name=@table_name;
set @sql=left(@sql,char_length(@sql)-1);
select nullif ('please stand by...',@sql:=concat(@sql,' from nums where id<=',@row_count,';')) info;
prepare statement from @sql;
execute statement;
commit;
