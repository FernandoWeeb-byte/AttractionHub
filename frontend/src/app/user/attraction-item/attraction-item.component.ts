import { Component, OnInit, Input } from '@angular/core';
import { faStar, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { AuthServiceService } from 'src/app/auth-service.service';

@Component({
  selector: 'app-attraction-item',
  templateUrl: './attraction-item.component.html',
  styleUrls: ['./attraction-item.component.sass']
})
export class AttractionItemComponent implements OnInit {

  faStar = faStar;
  faTrashAlt = faTrashAlt;

  constructor(private service: AuthServiceService) { }

  @Input() title:any
  @Input() urlImg:any
  @Input() score:any
  @Input() status:any
  token: any;
  ngOnInit(): void {
  }

  async delete(){
    this.token = window.localStorage.getItem('token')
    await this.service.deleteFromList(this.title, this.token)
  }

}
