<?php
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $website = $_POST['website'];
    $message = $_POST['message'];
 
    if(!empty($email) && !empty($message)){
     if(filter_var($email, FILTER_VALIDATE_EMAIL)){
        $receiver = "dhdbals9013@gmail.com";
        $subject ="From: $name <$email>";
        $body = "Name: $name\nEmail: $email\nPhone: $phone\nWebsite: $website\nMessage: $message\n\nRegards, \n$name";
        $sender = "From: $email";
  
        if(mail($receiver, $subject, $body, $sender)){
            echo "Your message has been sent";
        }else{
            echo "Failed to send an email";
        }
     }
     else{
         echo "Wrong email address format";
     }
    }
    else{
     echo "Email and message field are required";
    }
?>