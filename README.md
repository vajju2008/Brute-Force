[defense-how-it-works-6 (2).csv](https://github.com/user-attachments/files/26540720/defense-how-it-works-6.2.csv)
Defense,How It Works,Example
Parameterized Queries,"Treats input as raw data, not code","cursor.execute(""SELECT * FROM users WHERE username=? AND password=?"", (u, p))"
Stored Procedures,Encapsulates SQL logic in DB,"CALL check_login(u, p)"
Input Validation,Rejects suspicious characters,"Block ', --, ;"
Least Privilege,Restrict DB user rights,No DROP/ALTER permissions
Error Handling,Hide DB errors from users,"Show generic ""Invalid login"""
Web Application Firewall (WAF),Detects and blocks injection attempts,Rules for SQL keywords[payload-type-6 (1).csv](https://github.com/user-attachments/files/26540725/payload-type-6.1.csv)
Payload,Type,Effect
' OR '1'='1,Tautology,Always true → bypass login
' OR '1'='1' --,Tautology + Comment,Ignores rest of query
admin' --,Inline Comment,"Forces query to match ""admin"""
"' UNION SELECT null,null,null --",UNION Injection,Extracts data from other tables
' OR EXISTS(SELECT * FROM users) --,Boolean-based,Confirms table existence
"1' AND SUBSTR(password,1,1)='a' --",Blind Injection,Extracts data character by character
