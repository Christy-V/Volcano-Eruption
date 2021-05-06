<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page import="com.christy.bean.Shares"%>
<%@page import="java.util.ArrayList"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1>Share Details</h1>

	<table border="1">
		<tr>
			<th>SHARE_ID</th>
			<th>SHARE_Name</th>
			<th>TYPE</th>
			<th>MARKET_VALUE</th>
		</tr>

		<%
			ArrayList<Shares> shList = (ArrayList) session.getAttribute("shares");
			for (Shares sh : shList) {
		%>
		<tr>
			<td><%=sh.getShare_id()%></td>
			<td><%=sh.getShare_name()%></td>
			<td><%=sh.getType()%></td>
			<td><%=sh.getMarket_value()%></td>
		</tr>

		<%
			}
		%>

	</table>
		<br>
	<br>
	<a href="./index.jsp">Go To Main Page</a>
</body>
</html>