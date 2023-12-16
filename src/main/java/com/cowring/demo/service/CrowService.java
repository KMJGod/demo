package com.cowring.demo.service;

import com.cowring.demo.entity.top10_up;
import com.cowring.demo.repository.CrowRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CrowService {

    @Autowired
    private CrowRepository crowRepository;

    public List<top10_up> crowindexForm() {

        return crowRepository.findAll();
    }

}
