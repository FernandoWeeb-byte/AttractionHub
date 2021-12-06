import { Component, OnInit,Input, Output, EventEmitter } from '@angular/core';
import { AuthServiceService } from 'src/app/auth-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-attraction',
  templateUrl: './attraction.component.html',
  styleUrls: ['./attraction.component.sass']
})
export class AttractionComponent implements OnInit {

  constructor(private service: AuthServiceService, private router: Router) { }

  @Output() obj = new EventEmitter<any>();
  id:any;
  att:any;
  async ngOnInit(): Promise<void> {
    this.id = window.localStorage.getItem('id')
    const token = window.localStorage.getItem('token')
    try{
      if(this.router.url == "/"){
        this.att = await this.service.searchId(this.id)
      }
      else{
        this.att = await this.service.searchListId(token,this.id)
      }
      
    }catch(error){
      console.log(error)
    }
    
    this.att = this.att.data
    
    this.obj.emit({
      title: this.att.title,
      score: this.att.score,
      like: this.att.like ,
      status: this.att.status 
    });
    console.log(this.att.status)
  }

  res:any
  async onClick(){
    try{
      console.log(this.att.genre)
      this.res = await this.service.addToList(this.att)
    }catch(error){
      console.log(error)
    }
    this.router.navigate(['list'])
  }

}
