function ClearTxt(){
   location.reload();
}


function HandleCaseTxt(){
   var CaseFile = document.getElementById("ShowCase").innerHTML;
   var CaseStr = CaseFile.split("，");
   return CaseStr;

}

function HandleTestTxt(){
   var TestFile = document.getElementById("ShowRes").innerHTML;
   var TestStr = TestFile.split("，");
   return TestStr;
}

function CompTxt(){
   var CaseStr= HandleCaseTxt();
   var TestStr= HandleTestTxt();
   var Caselen=CaseStr.length;
   var Testlen=TestStr.length;
   if(CaseStr=="" || TestStr==""){
      alert("请填写表单并上传文件");
   }
   else if (Caselen!=Testlen) {
      alert("请检查标点格式和符号！");
   }
   else{
      var row=0;
      while(row<=Caselen){
         if (CaseStr[row]!=TestStr[row]) {
            var tempR = document.getElementById("ShowRes").innerHTML;
            tempR = tempR.replace(TestStr[row],"<font style='background:red'>" + TestStr[row] + "</font>");
            document.getElementById("ShowRes").innerHTML=tempR;
            var tempC = document.getElementById("ShowCase").innerHTML;
            tempC = tempC.replace(CaseStr[row],"<font style='background:yellow'>" + CaseStr[row] + "</font>");
            document.getElementById("ShowCase").innerHTML=tempC;
            row++;
         }
         else{
            row++;
            if(row>Caselen)
            alert("检查完成！")
         }
      }
   }
}
