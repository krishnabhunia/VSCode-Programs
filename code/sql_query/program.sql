SELECT employee_id,
       department,
       salary,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
       NTILE(4) OVER (PARTITION BY department ORDER BY salary DESC) AS quartile
FROM employees;


/*

employee_id	department	salary	dense_rank	rank	row_num	    quartile
    1	            HR	        90000	    1	      1	      1	            1
    2	            HR	        85000	    2	      2	      2	            1
    3	            HR	        85000	    2	      2	      3	            2
    4	            HR	        75000	    3	      4	      4	            2
    5	            Sales	    100000	    1	      1	      1	            1
    6	            Sales	    95000	    2	      2	      2	            1

*/