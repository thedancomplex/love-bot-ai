LOG_NAME=delay_num.log
THE_NUM=1

X=$(< $LOG_NAME)

Y=$(expr $X + 1)

RET=0

if [ $Y -gt $1 ]
then
  RET=1
  Y=0
fi

echo $Y > $LOG_NAME

cat $LOG_NAME
