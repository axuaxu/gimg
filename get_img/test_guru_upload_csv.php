<?php
echo getcwd();
echo "<br>name".$_FILES['file']['name'][0]; 
 echo "<br>size".$_FILES['file']['size'][0];
echo "<br>type".$_FILES['file']['type'][0];
echo "<br>tmp_name".$_FILES['file']['tmp_name'][0]."<br>";
   

for($i=0; $i < count($_FILES['file']['name']);$i++)
        {
echo $_FILES['file']['name'][$i] ."==<br>";
$name=$_FILES['file']['name'][$i];

if( $name != "" )
{     
   $key_end=strpos($name,".htm");
   $keyword = substr($name,0,$key_end);
   copy( $_FILES['file']['tmp_name'][$i], "/home2/tocityho/public_html/phpcode/koala/uploads/".$_FILES['file']['name'][$i] ) or 
           die( "Could not copy file!".$_FILES['file']['name'][$i]);
  echo $i." copied ".$name."==<br>"; 
  
  $row = 1;
  $csvName = "/home2/tocityho/public_html/phpcode/koala/uploads/".$_FILES['file']['name'][$i] ;
  $localPath = "/home2/tocityho/public_html/gurukoala/wp-content/uploads/2015/img01/" ;
  echo $csvName."<br>";
if (($handle = fopen($csvName, "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
        echo "<p> $num fields in line $row: <br /></p>\n";
        $row++;
        for ($c=0; $c < $num; $c++) {
            //echo $c."==".$data[$c] . "<br />\n";
			$imageURL = $data[0];
			$localName = $data[1];
        }
		$localFile = $localPath . $localName;
		//echo $imageURL."== localname:".$localName."== localfile:".$localFile."\n";
		copy($imageURL, $localFile);
		echo "copyied from ".$imageURL." to ".$localFile."\n";
    }
    fclose($handle);
}
  
  
}
else
{
    die($i."No file specified!".$_FILES['file']['name'][$i]);
}
}
?>
<html>
<head>
<title>Uploading Complete</title>
</head>
<body>
<h2>Uploaded File Info:</h2>
<ul>
<li>Sent file: <?php echo $_FILES['file']['name'];  ?>
<li>File size: <?php echo $_FILES['file']['size'];  ?> bytes
<li>File type: <?php echo $_FILES['file']['type'];  ?>
</ul>
</body>
</html>