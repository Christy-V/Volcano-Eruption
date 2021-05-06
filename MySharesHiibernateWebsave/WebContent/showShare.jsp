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
	<c:if test="${not empty shares }">
		<table border="1">
			<tr>
				<th>SHARE_ID</th>
				<th>SHARE Name</th>
				<th>TYPE</th>
				<th>MARKET_VALUE</th>
			</tr>

			<tr>
				<td>${shares.share_id}</td>
				<td>${shares.share_name }</td>
				<td>${shares.type }</td>
				<td>${shares.market_value}</td>
			</tr>

		</table>
	</c:if>
	
	<c:if test="${empty shares }">
		<%="Shares does not exist" %>
	</c:if>
	
	<br><br>
	<a href="./index.jsp">Go to Main Page</a>
</body>
</html>