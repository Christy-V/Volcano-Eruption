package com.christy.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.christy.model.service.SharesService;
import com.christy.model.service.SharesServiceImpl;


public class UpdateSharesController extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session=request.getSession();
		
		SharesService shareService=new SharesServiceImpl();
		String message=null;
		if(shareService.updateMarketValues(Integer.parseInt(request.getParameter("mvalue")),request.getParameter("sId")))
			message="Shares Updated Succesfully";
		else
			message="Shares Updated Failed";
		
		
		session.setAttribute("msg", message);
		
		response.sendRedirect("./output.jsp");
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
