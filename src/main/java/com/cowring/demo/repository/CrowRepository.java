package com.cowring.demo.repository;

import com.cowring.demo.entity.top10_up;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CrowRepository extends JpaRepository<top10_up, Integer > {
}
