package com.christy.model.service;

import java.util.ArrayList;

import com.christy.bean.Shares;

public interface SharesService {
	ArrayList<Shares> getAllShares();
	boolean insertShares(Shares share);
	boolean deleteShares(String share_id);
	boolean updateMarketValues(int market_values,String share_id);
	Shares searchSharesById(String share_id);
	ArrayList<Shares> selectShareService(int mvalue);
}
