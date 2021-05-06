package com.christy.model.persistence;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.query.Query;
import com.christy.bean.Shares;
import com.christy.util.MySessionFactoryClass;

public class SharesDaoImpl implements SharesDao {

	@Override
	public ArrayList<Shares> getShare() {
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		//HQL
		Query<Shares> query=session.createQuery("from Shares");
		List<Shares> shares=query.getResultList();

		transaction.commit();

		session.close();

		return (ArrayList<Shares>)(shares) ;
	}

	@Override
	public boolean insertRecord(Shares share) {
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		session.save(share);

		transaction.commit();

		session.close();

		return true;
	}

	@Override
	public boolean deleteRecord(String share_id) {
		// TODO Auto-generated method stub
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		Shares share=session.get(Shares.class, share_id);
		session.delete(share);
		
		
		transaction.commit();

		session.close();

		return true;
	}

	@Override
	public Shares searchById(String share_id) {
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		Shares shares=session.get(Shares.class, share_id);

		transaction.commit();

		session.close();

		return shares;
	}

	@Override
	public boolean updateMarketValues(int market_values, String share_id) {
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		Shares shares=session.get(Shares.class, share_id);
		boolean status=false;
		if(shares!=null){
			shares.setMarket_value(market_values);
			
			status=true;
		}

		transaction.commit();

		session.close();

		return status;
	}
	@Override
	public ArrayList<Shares> selectShare(int mvalue) {
		MySessionFactoryClass sessionFactory=new MySessionFactoryClass();

		SessionFactory factory=sessionFactory.getSessionFactory();
		
		Session session = factory.openSession();

		Transaction transaction = session.beginTransaction();

		//HQL
		Query<Shares> query=session.createQuery("from Shares where market_value > :mvalue");
		System.out.println(mvalue);
		query.setParameter("mvalue", mvalue);
		List<Shares> shares=query.getResultList();

		transaction.commit();

		session.close();

		return (ArrayList<Shares>)(shares) ;
	}

}
