package com.christy.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.christy.bean.Shares;
import com.christy.model.service.SharesService;
import com.christy.model.service.SharesServiceImpl;


public class SearchShares extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session=request.getSession();
		
		SharesService sharesService=new SharesServiceImpl();
		Shares shares=sharesService.searchSharesById(request.getParameter("share_id"));
	
		session.setAttribute("shares", shares);
		response.sendRedirect("./showShare.jsp");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
