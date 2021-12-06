import { Component, OnInit, Input } from '@angular/core';
import { faStar, faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-attraction-item',
  templateUrl: './attraction-item.component.html',
  styleUrls: ['./attraction-item.component.sass']
})
export class AttractionItemComponent implements OnInit {

  faStar = faStar;
  faTrashAlt = faTrashAlt;

  constructor() { }

  @Input() title:any
  @Input() urlImg:any
  @Input() score:any
  @Input() status:any
  ngOnInit(): void {
  }

}
