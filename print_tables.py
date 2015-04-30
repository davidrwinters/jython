from java.sql import DriverManager
from java.lang import Class
from java.util import Properties

url    = 'jdbc:splice://localhost:1527/splicedb'
driver = 'org.apache.derby.jdbc.ClientDriver'
props  = Properties()
props.setProperty('user', 'APP')
props.setProperty('password', 'APP')
jcc    = Class.forName(driver).newInstance()
conn   = DriverManager.getConnection(url, props)
stmt   = conn.createStatement()
rs     = stmt.executeQuery("select * from sys.systables")

rowCount = 0
while (rs.next() and rowCount < 10) :
    rowCount += 1
    print "Record=[" + str(rowCount) + \
            "] id=[" + rs.getString('TABLEID') + \
            "] name=[" + rs.getString('TABLENAME') + \
            "] type=[" + rs.getString('TABLETYPE') + "]"

rs.close()
stmt.close()
conn.close()
