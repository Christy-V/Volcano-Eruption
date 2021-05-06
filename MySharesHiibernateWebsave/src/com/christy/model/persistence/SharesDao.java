package com.christy.model.persistence;

import java.util.ArrayList;

import com.christy.bean.Shares;

public interface SharesDao {
	ArrayList<Shares> getShare();
	boolean insertRecord(Shares share);
	boolean deleteRecord(String share_id);
	Shares searchById(String share_id);
	boolean updateMarketValues(int market_values,String share_id);
	ArrayList<Shares> selectShare(int mvalue);
}
