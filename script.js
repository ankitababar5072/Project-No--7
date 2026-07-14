const tweet=document.getElementById("tweet");

const count=document.getElementById("charCount");

tweet.addEventListener("input",()=>{

count.innerText=tweet.value.length;

});

function clearText(){

tweet.value="";

count.innerText=0;

tweet.focus();

}