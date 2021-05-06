<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>

		<table border="1">
			<tr>
				<th>SHARE_ID</th>
				<th>SHARE Name</th>
				<th>TYPE</th>
				<th>MARKET_VALUE</th>
			</tr>
<c:forEach items="${shares}" var="shl">
			<tr>
				<td>${shl.share_id}</td>
				<td>${shl.share_name }</td>
				<td>${shl.type }</td>
				<td>${shl.market_value}</td>
			</tr>
</c:forEach>
		</table>

	
	<br><br>
	<a href="./index.jsp">Go to Main Page</a>
</body>
</html>