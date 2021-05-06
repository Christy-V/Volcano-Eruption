package com.christy.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.christy.bean.Shares;
import com.christy.model.service.SharesService;
import com.christy.model.service.SharesServiceImpl;

public class DisplaySelectedController extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session=request.getSession();
		
		SharesService sharesService=new SharesServiceImpl();
		ArrayList<Shares> shList=sharesService.selectShareService(Integer.parseInt(request.getParameter("mvalue")));
		
		session.setAttribute("shares", shList);
		
		response.sendRedirect("./showSelectedShares.jsp");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
