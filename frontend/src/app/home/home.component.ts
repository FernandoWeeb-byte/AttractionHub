import { Component, Input, OnInit } from '@angular/core';
import { AuthServiceService } from '../auth-service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.sass']
})
export class HomeComponent implements OnInit {

  constructor(private service: AuthServiceService) {
    
   }
  
  isLogged:boolean = false
 
  
  token:any
  res:any
  user:any
  async ngOnInit(): Promise<void> {
    this.token = window.localStorage.getItem('token')
    try{
      this.res = await this.service.isLogged(this.token)
    }catch(error){
      console.log(error)
    }
    console.log(this.token)
    console.log(this.res)
    if(this.res.login){
      console.log("entrou aqui")
      this.isLogged = true
      this.user = this.res.user
    }
    else{
      console.log("entrou")
      this.isLogged = false
    }
    console.log(this.isLogged);
  }

}
