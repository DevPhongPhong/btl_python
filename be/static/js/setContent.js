id=location.pathname.substring(6,location.pathname.length)

$.ajax({
    url:`/api/post/${id}`,
    type:'GET',
    success:(res)=>{
        btl_content = document.getElementById('btl_content')
        btl_content.innerHTML =`<div class="main-figure">
        <a href="#"><img src="${res.main_image[0]}" alt="Blog"></a>
        </div>
        <div class="blog-content">
        <ul class="entry-meta">
            <li><a href="#"><i class="fas fa-clock"></i>${res.created_time[0]}</a></li>
            <li><a href="#"><i class="fas fa-user"></i>by <span>${res.author[0]}</span></a></li>
        </ul>
        <h3 class="item-title"><a href="/post/${res.id[0]}"></a>${res.title}</h3>
        ${res.full_content[0]}
        </div>`

        btl_post_title = document.getElementById('btl_post_title')
        btl_post_title.innerHTML+=(": "+res.title)
    }
})
