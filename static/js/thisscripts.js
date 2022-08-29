

// QR view js
const qricount = document.getElementsByClassName("qrcount")
const qracount = document.getElementsByClassName("qraddcount")
const qrrcount = document.getElementsByClassName("qrremovecount")
const qrdelete = document.getElementsByClassName("qrorderdelete")

var qrupdateBtns = document.getElementsByClassName('qrupdate-cart')
var qrupdateBtn = document.getElementsByClassName('qrupdate-item-cart')
for (let i=0; i < qrupdateBtns.length; i++){
    let qrcount = 0;
    qrupdateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var productprice = this.dataset.price
        console.log('productId:',productId, 'action:',action, 'productprice:',productprice)
        console.log('USER:',user)
       if(productId){
            qrcount ++;
            console.log(productId);
            qrupdateBtns[i].textContent = '+'
            qricount[i].textContent = 'newly added:' + qrcount;
       }
       
        if (user =='AnonymousUser'){
            console.log('table is not logged in')
            qrupdateUserOrder(productId, action, productprice)
        }else{
            qrupdateUserOrder(productId, action, productprice)
        }
    })
}

for (var i=0; i< qrupdateBtn.length; i++){
    let qrcount = 0;
    qrupdateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var productprice = this.dataset.price
        console.log('productId:',productId, 'action:',action, 'productprice:',productprice)
        // if(action = 'add'){
            if(action === 'add'){
                qrcount ++;
                console.log(productId);
                qracount[i].textContent = 'added:' + qrcount;
            }
        if(action === 'remove'){
            qrcount ++;
            console.log(productId);
            qrrcount[i].textContent = 'removed:' + qrcount;
        }
        if(action === 'delete'){
            
            console.log(productId);
            qrrcount[i].textContent = 'Items deleted sucessfully';
        }
        if (user =='AnonymousUser'){
            console.log('table is not logged in')
            qrupdateUserOrders(productId, action, productprice)
        }else{
            qrupdateUserOrders(productId, action, productprice)
        }
    })
}
function qrupdateUserOrder(productId, action, productprice){
    console.log('table is logged in, sending data..')
    var price = {
        'productprice':productprice,
    }
    var url = '/qrupdate_item/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action, 'form':price})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
        // location.reload()
    })
}
function qrupdateUserOrders(productId, action, productprice){
    console.log('table is logged in, sending data..')
    var price = {
        'productprice':productprice,
    }
    var url = '/qrupdate_item/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action, 'form':price})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:',data)
    })
}

