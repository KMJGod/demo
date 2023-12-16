package com.cowring.demo.controller;

import com.cowring.demo.service.CrowService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class crowController {

    @Autowired
    private CrowService crowService;

    @GetMapping("/demo/crowindex")
    public String crowindexForm(Model model){

        model.addAttribute("list", crowService.crowindexForm());

        return  "crowindex";
    }
}
