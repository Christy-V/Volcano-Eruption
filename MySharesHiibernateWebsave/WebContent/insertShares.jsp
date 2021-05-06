<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<h1>Insert Share Details</h1>
<form action="./save" method="post">
	Enter Share ID : <input type="text" name="id"><br><br>
	Enter Share Name : <input type="text" name="sname"><br><br>
	Enter Share type : <input type="text" name="type"><br><br>
	Enter Market Value : <input type="text" name="mvalue"><br><br>
	<input type="submit" value="Save Share">
</form>
<br><br>
<a href="./index.jsp">Go to Main Menu</a>
</body>
</html>