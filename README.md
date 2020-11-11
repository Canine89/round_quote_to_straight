# round_quote_to_straight
파일의 둥근 따옴표 `’`, `‘`, `“`, `”`를 모두 곧은 따옴표 `'`, `"`로 바꿔주는 파이썬 프로그램입니다. 물론 [find > replace] 4번 실행하면 되긴 합니다. 하지만 실습 파일의 개수가 많아지면 이마저도 노동이고 심지어는 코드에서 둥근 따옴표가 잘 보이지 않아 놓치고 프로그램을 재실행하면서 '내가 뭘 잘못 입력한거지...'하는 경우가 다반사더군요. 그래서 만들었습니다.


## 사용 방법
```
> python find_replace.py
> <full-path-of-your-file, 파일의 절대 경로 입력해 주세요(코드 에디터의 copy full path... 사용 권장)>
```

해당 파일의 둥근 따옴표를 모두 바꾸어 곧은 따옴표로 저장해 줍니다. 약 30개 이상의 파일에 적용해 봤습니다. 우선은 잘 실행되어 파일의 원본 유지는 굳이 할 필요가 없다 판단했습니다. 혹시 문제 있으면 이슈 등록해 주세요.

## 특장점?
- 코드를 보시면 아시겠지만 아무 입력 없이 줄바꿈되는 것도 그대로 유지해 줍니다.
- 변경 후 자동 저장을 해주므로 1번이라도 손이 덜갑니다.
