<?php

    if ($_POST['username'] == 'admin' && $_POST['password'] == '123') {
        echo 'Welcome to admin';
    } else {
        echo 'Error. Verify your username and password';
    }
