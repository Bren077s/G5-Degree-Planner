<?php
require "header.php";
?>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Degree Planner</title>

    <!-- Bootstrap Core CSS -->
    <link href="../vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../vendor/metisMenu/metisMenu.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../dist/css/degree_planner.css" rel="stylesheet">
    <!-- Custom Fonts -->
    <link href="../vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <?php
	require "navigation.php";
	?>
        <!-- Page Content -->
        <div id="page-wrapper">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <h1 class="page-header">Mechanical Engineering</h1>
						<div class="panel-body">
							<a href="http://blogs.mtu.edu/me-undergrad/files/2017/02/BSME-FEB-2017-201702CatYr-020717-GREEN-with-notes-Colored.pdf">Senior Design Flowchart</a><br>
							<a href="http://blogs.mtu.edu/me-undergrad/files/2017/02/BSME-ENT-FEB-2017-201702CatYr-020717-PINK-with-notes-Colored.pdf">Enterprise Flowchart</a><br>
							<h2>Classes</h2>
							<?php
							require "mysql_connect.php";

							$sql ="SELECT course_name FROM courses WHERE dept='Mechanical Eng. - Engrg. Mech.   '";
							$result=mysqli_query($connection, $sql);
							$rows = $result->fetch_all();
							foreach($rows as $row){
							echo $row[0]."<br>";
							}
							?>
							

						</div>
                    </div>
                    <!-- /.col-lg-12 -->
                </div>
                <!-- /.row -->
            </div>
            <!-- /.container-fluid -->
        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- jQuery -->
    <script src="../vendor/jquery/jquery.min.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="../vendor/bootstrap/js/bootstrap.min.js"></script>

    <!-- Metis Menu Plugin JavaScript -->
    <script src="../vendor/metisMenu/metisMenu.min.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="../dist/js/degree_planner.js"></script>

</body>

</html>
