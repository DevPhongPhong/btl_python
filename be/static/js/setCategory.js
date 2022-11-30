$.ajax({
    url: '/api/post/get-five-category-random',
    type: 'GET',
    success: function (data) {
        const btl_category = document.getElementById('btl_category')
        btl_category.innerHTML =''
        for(i=0;i<5;i++){
            btl_category.innerHTML+=`<li>
                                        <a href="/category/${data[i].id[0]}">${data[i].name[0]}
                                            <span></span>
                                        </a>
                                    </li>`
        }
    }
})