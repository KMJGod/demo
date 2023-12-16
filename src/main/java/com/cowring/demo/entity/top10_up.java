package com.cowring.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class top10_up{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String n_date;
    private String company;
    private String price;
    private String change;
    private String change_price;
    private String percent;

    public Integer getId() {
        return id;
    }

    public String getN_date() {
        return n_date;
    }

    public String getCompany() {
        return company;
    }

    public String getPrice() {
        return price;
    }

    public String getChange() {
        return change;
    }

    public String getChange_price() {
        return change_price;
    }

    public String getPercent() {
        return percent;
    }
}
