TC-SQL-01    

title : Duplicate user is handled correctly



API behaviour :
   
   method : POST 
   endpoint : /users/

   json body {
      "name":"qa-test"
      "email":"qa@gmail.com
   }

   json body {
      "name":"qa-test"
      "email":"qa12@gmail.com
   }

   json body {
      "name":"qa-test"
      "email":"qa123@gmail.com
   }

   expected result :
        status code : 201 created 
    
         

   actual result : 
        status_code :201 created 




SQL query {
    select id,name,email from users where name="qa-test";
}


db behaviour 
    expected result : it shows users name where name equal to qa-test ,it should show 3 users with same name and different email 

    actual result : it shows users name where name equal to qa-test ,shows 3 user with same name and different email 

status : PASS