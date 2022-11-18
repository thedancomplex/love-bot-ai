REPLY_NUM=2
cd love-bot-ai/delays/

RET=./check_resp_num.sh $REPLY_NUM

if [ $RET -eq 1 ]
then
  ./do_delay.sh
fi
