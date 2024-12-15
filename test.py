import sqlite3

conn = sqlite3.connect('./db.sqlite3')
cursor = conn.cursor()

cursor.execute("BEGIN TRANSACTION;")

queries = [
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Intrest Received','580','20240625','KDDT','SBI BANK','SBI BANK','0','20240625','','27','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20240704','KDDT','M. SENTHIL KUMAR','ICICI BANK (IMPS)','418620929161','20240704','','28','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20240712','KDDT','K. BALARAMAN','ICICI BANK (IMPS)','419407991504','20240712','','29','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','3200','20240715','KDDT','S. CHOKKAPPAN','CANARA BANK ( IMPS)','419717485991','20240715','','30','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','9750','20240719','KDDT','R. SRINIVASAN','ICICI BANK (IMPS)','420113696868','20240719','','31','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'KDDA Loan Received','40000','20240729','KDDT','KDDA','CANARA BANK (NEFT)','211240338741297','20240729','','32','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','16000','20240804','KDDT','M.Mohamed Ansar','ICICI BANK (IMPS)','45833718972','20240804','','33','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','16000','20240805','KDDT','K. PRAKASH','CANARA BANK (IMPS)','421877108326','20240805','','34','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12500','20240805','KDDT','B. RAJU','CANARA BANK (IMPS)','421817269450','20240805','','35','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12500','20240805','KDDT','B. RAJU','CANARA BANK ( IMPS)','421817269883','20240805','','36','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','25000','20240805','KDDT','S. JAYAVEL','ICICI BANK (IMPS)','12586717506','20240805','','37','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12500','20240805','KDDT','L. SEBESTIRAJ','ICICI BANK ( IMPS)','421821127251','20240805','','38','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','9500','20240806','KDDT','K. BALARAMAN','ICICI BANK (IMPS)','421910011293','20240806','','39','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20240806','KDDT','J. AROCKIASMY','ICICI BANK (IMPS)','458564480','20240806','','40','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','4400','20240810','KDDT','V. KRISHNAMOORTY','ICICI BANK (UPI)','458978795132','20240810','','41','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10750','20240812','KDDT','V. MOHAN','SBI BANK (UPI)','422510451387','20240812','','42','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','9750','20240911','KDDT','S.CHOKKAPPAN','CANARA BANK (IMPS)','425513876802','20240911','','43','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','3200','20240911','KDDT','A.GOVARTHANAN','ICICI BANK (IMPS)','425516449440','20240811','','44','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20240913','KDDT','M. SENTHIL KUMAR','ICICI BANK (IMPS)','425709892753','20240913','','45','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Intrest Received','362','20240925','Intrest Received','KDDT','SBI BANK','0','20240925','','46','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','4500','20241003','KDDT','A.GOVANRTANAN','ICICI Bank (imps)','427722748154','20241003','','47','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241010','KDDT','S. JAYAVEL','CANARA BANK (IMPS)','428413684790','20241010','','48','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12950','20241010','KDDT','V. MOHAN','SBI BANK ( UPI)','428422264083','20241010','','49','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12500','20241018','KDDT','V. MOHAN','CANARA Bank','13285589043','20241018','','50','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','5000','20241019','KDDT','G.JAISHANKAR','CANARA BANK','13292283564','20241019','','51','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241019','KDDT','V. MOHAN','CANARA BANK','13292343213','20241019','','52','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241019','KDDT','M. SENTHIL KUMAR','ICICI BANK (IMPS)','429312780026','20241019','','53','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241021','KDDT','B. RAJU','CANARA BANK','13307144468','20241021','','54','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','500','20241021','KDDT','K. PRAKASH','ICICI BANK (UPI)','429508914744','20241021','','55','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','500','20241021','KDDT','R. SRINIVASAN','ICICI BANK (IMPS)','429509212817','20241021','','56','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241021','KDDT','J. AROCKIASMY','ICICI BANK (UPI)','429594331635','20241021','','57','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241021','KDDT','L.SEBESTIRAJ','ICICI BANK (IMPS)','429515046213','20241021','','58','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','500','20241023','KDDT','S.SIVAKUMAR','CANARA BANK','13328376895','20241023','','59','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241023','KDDT','M.SENTHILKUMAR','ICICI BANK (IMPS)','429712023364','20241023','','60','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1000','20241024','KDDT','A.GOVANRTANAN','CANARA BANK','13338798653','20241024','','61','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1500','20241026','KDDT','S. MURUGESAN','ICICI BANK (UPI)','466684670985','20241026','','62','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','12500','20241027','KDDT','S. JAYAVEL','CANARA BANK (IMPS)','430111524759','20241027','','63','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','7250','20241104','KDDT','V. KRISHNAMOORTHY','ICICI BANK ( UPI)','467508861562','20241104','','64','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','5000','20241105','KDDT','G. JAISHANKAR','TMB BANK','1354385913389350','20241105','','65','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','1250','20241105','KDDT','G. JAISHANKAR','DBS BANK (UPI)','431038415838','20241105','','66','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','4200','20241106','KDDT','M. MOHAMED ANSAR','ICICI BANK (UPI)','431167389082','20241106','','67','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','G.JAISHANKAR','DBS BANK (UPI)','432658152730','20241121','','68','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','R. SRINIVASAN','ICICI BANK (IMPS)','43261531759','20241121','','69','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','M. MOHAMED ANSAR','ICICI BANK ( UPI)','432679853525','20241121','','70','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','20000','20241121','KDDT','V. GOVANRTANAN','CANARA BANK (IMPS)','432618557011','20241121','','71','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','V. MOHAN','SBI BANK (UPI)','432663451002','20241121','','72','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','20000','20241121','KDDT','L.SEBESTIRAJ','CANARA BANK (IMPS)','432620585879','20241121','','73','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','20000','20241121','KDDT','R. BALARAMAN','ICICI BANK (IMPS)','432618670052','20241121','','74','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','M. MOHAMED ANSAR','ICICI BANK (UPI)','4326940764477','20241121','','75','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','G. JAISHANKAR','TBM BANK (UTR)','3365059134400','20241121','','76','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','K. PRAKASH','ICICI BANK (IMPS)','432621080962','20241121','','77','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','R. SRINIVASAN','ICICI BANK (IMPS)','432621083885','20241121','','78','Transfer'",
    "insert into account_income (income_name,amount,date,reason,income_by,bankname,chequeordd,dateinbank,details,incid, mode)  select 'Donation','10000','20241121','KDDT','V. MOHAN','CANARA BANK (UPI)','469280555998','20241121','','79','Transfer'"
]

for query in queries:
    cursor.execute(query)

conn.commit()

conn.close()