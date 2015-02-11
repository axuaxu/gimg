<?php
$con = mysql_connect("localhost","tocityho_click","click1");
 $db = mysql_select_db("tocityho_wor3879",$con);
 $get=mysql_query("SELECT keyword FROM wp_koala_filename_log order by keyword");
 ?>
<html>
<body>
<h3>Step 1. Upload Files</h3>
Select a file to upload: <br />
<form action="test_guru_upload_csv.php" method="post"
                        enctype="multipart/form-data">
<input type="file" name="file[]" size="50" /><input type="file" name="file[]" size="50" /><input type="file" name="file[]" size="50" />
<input type="file" name="file[]" size="50" /><input type="file" name="file[]" size="50" />

<br /><br>
<input type="submit" value="Upload File" />
</form>
<p>
 
  




</body>
</html>