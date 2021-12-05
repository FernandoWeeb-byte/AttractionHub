import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from 'src/app/auth-service.service';
@Component({
  selector: 'app-my-list',
  templateUrl: './my-list.component.html',
  styleUrls: ['./my-list.component.sass']
})
export class MyListComponent implements OnInit {

  constructor(private service: AuthServiceService) { }
  type:any = 'all'
  token:any
  res:any
  user:any
  list:any
  async ngOnInit(): Promise<void> {
    this.token = window.localStorage.getItem('token')
    try{
      this.res = await this.service.isLogged(this.token)
    }catch(error){
      console.log(error)
    }
    console.log(this.token)
    console.log(this.res)
    this.user = this.res.user
    this.list = await this.service.getList(this.token, this.type)
    this.list = this.list.data
    
  }
    
  async onClick(tp:any){
    console.log(tp)
    this.list = await this.service.getList(this.token, tp)
    this.list = this.list.data
    console.log(this.list)
  }
  

}
