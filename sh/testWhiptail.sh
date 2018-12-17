#/bin/bash

#whiptail --title "rr_title" --yesno "test" 100 100

##创建一个基础的对话框
#whiptail --title "Test Message Box" --msgbox "Create a message box with whiptail. Choose Ok to continue." 10 60

##创建一个具有yes 和no 的对话框
#if (whiptail --title "Test Yes/No Box" --yesno "Choose between Yes and No." 10 60)then
#    echo "You chose Yes. Exit status was $?."
#else
#     echo "You chose No. Exit status was $?"
#fi

#whiptail --title "Test Free-form Input Box" --inputbox "What is your pet's name?" 10 60 Wigglebutt 3>&1 1>&2 2>&3
