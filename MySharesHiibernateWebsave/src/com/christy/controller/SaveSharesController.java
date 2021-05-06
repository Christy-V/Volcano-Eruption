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


public class SaveSharesController extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session=request.getSession();
		
		String Id=request.getParameter("id");
		String sn=request.getParameter("sname");
		String tp=request.getParameter("type");
		String mv=request.getParameter("mvalue");
		
		Shares shares=new Shares(Id, sn, tp, Integer.parseInt(mv));
		
		SharesService sharesService=new SharesServiceImpl();
		String message=null;
		if(sharesService.insertShares(shares))
			message="Shares Saved Successfully";
		else
			message="Shares Insertion Failed";
		
		
		session.setAttribute("msg", message);
		response.sendRedirect("./output.jsp");
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
