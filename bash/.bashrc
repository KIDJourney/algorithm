# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

vpn()
{
	python /home/acmclub/software/goagent/local/proxy.py
}

clean()
{
    echo Are you sure to delete all non-cpp files??
    cnt=0
    arr=()
    for i in *; do
        if [ "${i##*.}" != "cpp" ] && ! [ -d "$i" ]; then 
            arr[$cnt]=$i
            cnt=$((cnt+1))

            if [ $cnt -le 10 ]; then echo $i; fi
        fi
    done

    if [ $cnt -gt 10 ]; then echo ...; fi

    read choice
    if [ "$choice" != "y" ]; then return; fi

    for i in ${arr[@]}; do
        rm $i
    done
}
