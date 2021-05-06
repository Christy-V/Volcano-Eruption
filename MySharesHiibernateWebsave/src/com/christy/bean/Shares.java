package com.christy.bean;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Shares {
	@Id
	private String share_id;
	private String share_name;
	private String type;
	private int market_value; 

	public Shares() {
		
	}
	public Shares(String share_id ,String share_name,String type,int market_value) {
		super();
		this.share_id = share_id;
		this.share_name = share_name;
		this.type = type;
		this.market_value = market_value;	
	}
	public String getShare_id() {
		return share_id;
	}
	public void setShare_id(String share_id) {
		this.share_id = share_id;
	}
	public String getShare_name() {
		return share_name;
	}
	public void setShare_name(String share_name) {
		this.share_name = share_name;
	}
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public int getMarket_value() {
		return market_value;
	}
	public void setMarket_value(int market_value) {
		this.market_value = market_value;
	}
	@Override
	public String toString() {
		return "Shares [share_id=" + share_id + ", share_name=" + share_name + ", type=" + type + ", market_value="
				+ market_value + "]";
	}
}
