import { Component, OnInit } from '@angular/core';
import { AuthServiceService } from 'src/app/auth-service.service';
import { faThumbsUp, faThumbsDown } from '@fortawesome/free-solid-svg-icons'

@Component({
  selector: 'app-attraction-info',
  templateUrl: './attraction-info.component.html',
  styleUrls: ['./attraction-info.component.sass']
})
export class AttractionInfoComponent implements OnInit {
  faThumbsUp = faThumbsUp;
  faThumbsDown = faThumbsDown;
  constructor(private service: AuthServiceService) { }
  token:any
  res:any
  user:any
  value: any;
  scores = [1,2,3,4,5,6,7,8,9,10]
  like: any;
  status: any;
  score:any
  obj: any;
  
  async ngOnInit(): Promise<void> {
    this.token = window.localStorage.getItem('token')
    try{
      this.res = await this.service.isLogged(this.token)
    }catch(error){
      console.log(error)
    }
    if(this.res.login){
      this.user = this.res.user
    }

    this.like = this.obj.like;
    this.score = this.obj.score;
    this.status = this.obj.status;
  }

  onChangeStatus(selected: any) {
    this.service.updateList(this.token,this.obj.title, null, selected,null);
  }

  onChangeScore(selected: any) {
    console.log(selected)
    this.service.updateList(this.token, this.obj.title, selected, null, null);
  }
  
  onLike(n:any){
    if(n === "1"){
      this.like = true
      
    }
    else if(n === "2"){
      this.like = false
    }
    this.service.updateList(this.token, this.obj.title, null, null, this.like);
  }

}
