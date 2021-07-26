async function getData(){
    var response = await fetch('https://api.github.com/users/adion81');
    var data = await response.json();
    var image = document.getElementById('avatar');
    image.src=data.avatar_url;

    var name = data.login;
    var followersCount = data.followers;
    console.log(followersCount);

    var followersP = document.getElementById("followers");
    followersP.innerText = name + ' has ' + followersCount + ' followers';

}