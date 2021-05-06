package com.christy.model.service;

import java.util.ArrayList;

import com.christy.bean.Shares;
import com.christy.model.persistence.SharesDao;
import com.christy.model.persistence.SharesDaoImpl;

public class SharesServiceImpl implements SharesService {
	private SharesDao sharesDao=new SharesDaoImpl();
	@Override
	public ArrayList<Shares> getAllShares() {
		// TODO Auto-generated method stub
		return sharesDao.getShare();
	}

	@Override
	public boolean insertShares(Shares share) {
		// TODO Auto-generated method stub
		return sharesDao.insertRecord(share);
	}

	@Override
	public boolean deleteShares(String share_id) {
		// TODO Auto-generated method stub
		return sharesDao.deleteRecord(share_id);
	}

	@Override
	public boolean updateMarketValues(int market_values, String share_id) {
		// TODO Auto-generated method stub
		return sharesDao.updateMarketValues(market_values, share_id);
	}

	@Override
	public Shares searchSharesById(String share_id) {
		// TODO Auto-generated method stub
		return sharesDao.searchById(share_id);
	}
	@Override
	public ArrayList<Shares>  selectShareService(int mvalue) {
		// TODO Auto-generated method stub
		return sharesDao.selectShare(mvalue);
	}
}
