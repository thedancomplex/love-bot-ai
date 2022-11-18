LOG_NAME=delay_num.log
THE_NUM=1

X=$(< $LOG_NAME)

Y=$(expr $X + 1)

echo $Y > $LOG_NAME

cat $LOG_NAME
