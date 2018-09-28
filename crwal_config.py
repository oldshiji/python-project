#爬取网页配置文件


Accept='application/json, text/javascript, */*; q=0.01'
Accept_Encoding='gzip, deflate, br'
Accept_Language='zh-CN,zh;q=0.8'
Connection='keep-alive'
Content_Length='43'
Content_Type='application/x-www-form-urlencoded; charset=UTF-8'
Cookie='JSESSIONID=ABAAABAAAIAACBIA7ADB3F1300369255127382E8505E401; user_trace_token=20180118092924-043866d3-fbef-11e7-a47d-5254005c3644; LGUID=20180118092924-04386d42-fbef-11e7-a47d-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Ks0000amqZra9B-65LBLMoPL91sXjYycsTuI8o4Uybt1KiKBgkXraD5womUQy3HL7et_rQZqsVt4UZ2CgjzuDCImVhNM7DZlC4sD-6gMUwOlQDuySxZcgdyE4vJqHAX4ADj9rrmxFDnkkoYiTGn4etNCeqc4ZXdYKr33MoWYmmAj7exIcs.Db_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzdT52h881gE4U_-xHbHz3x5Gse5gj_L3x5I9vX8Zdtt5M33xg4mIqp-muCyr5uvNe70.U1Yk0ZDqs2v4VnL30ZKGm1Yk0Zfqs2v4VnL30A-V5HcsP0KM5yF8nj00Iybqmh7GuZR0TA-b5HD40APGujYdrfKVIjYknjD4g1DsnHIxnH0zndt1njDdg1nvnjD0pvbqn0KzIjY3nWD0uy-b5HDYn1PxnH6krHNxnWDsrHPxnHTsnj7xnW04nWb0mhbqnW0Y0AdW5HTsP1fzPWmkP-tLnjT4PjfdP1PxnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5HD0uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1YYPWTLPHR1nW0krjnvn1msPHcs0ZF-TgfqnHRkPWc1rjbdP1fzPsK1pyfqmH6zrHc4mhRsnj01ujDsr0KWTvYqnYPKnY7APDw7PbwaPRwjPfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nH6vrHIxn0Ksmgwxuhk9u1Ys0AwWpyfqnWm3PjndPjRv0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqn1D4PHD%26ck%3D8391.1.70.314.570.323.560.498%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26us%3D1.0.2.0.1.301.0%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn%26inputT%3D10903%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_hz_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; _gid=GA1.2.912493768.1516238968; _ga=GA1.2.918918506.1516238968; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516238968,1516238975; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516239302; LGSID=20180118092931-083a3997-fbef-11e7-a548-525400f775ce; LGRID=20180118093458-cb581180-fbef-11e7-a47d-5254005c3644; SEARCH_ID=339fd17a996445c0bea8449479e4b3df'
Host='www.lagou.com'
Origin='https://www.lagou.com'
Referer='https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?oquery=Python&fromSearch=true&labelWords=relative'
User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
X_Anit_Forge_Code='0'
X_Anit_Forge_Token='None'
X_Requested_With='XMLHttpRequest'

#请求的url地址
Request_URL='https://www.lagou.com/jobs/positionAjax.json'
#请求的参数
needAddtionalResult=False
isSchoolJob=0
