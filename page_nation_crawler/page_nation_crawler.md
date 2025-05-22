# ページをめくるクローラー
ページを1~5まで自動的にめくるクローラーを作成せよ。なお、サーバー負荷を分散するため各自以下の店舗リンクから適当に1つ選んでURLに使ってください。

[ハンバーグ](https://tabelog.com/tokyo/A1304/A130402/13041176/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=5)  
[うどん](https://tabelog.com/tokyo/A1310/A131003/13000629/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=4)  
[たいやき](https://tabelog.com/tokyo/A1307/A130702/13002775/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=2)  
[パスタ](https://tabelog.com/tokyo/A1304/A130401/13123990/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=4)  
[カレー](https://tabelog.com/tokyo/A1302/A130201/13020091/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=5)  
[ステーキ](https://tabelog.com/tokyo/A1316/A131603/13042320/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=3)

ヒント
```python copy
# 以下のPG=の部分を固定値でなくて1~5の値をとる変数にして繰り返す。

urllib.request.urlopen('https://tabelog.com/tokyo/A1304/A130402/13041176/dtlrvwlst/COND-0/smp1/?smp=1&lc=0&rvw_part=all&PG=1')

```
