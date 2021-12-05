import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-attraction-item',
  templateUrl: './attraction-item.component.html',
  styleUrls: ['./attraction-item.component.sass']
})
export class AttractionItemComponent implements OnInit {

  constructor() { }

  @Input() title:any
  @Input() urlImg:any
  @Input() score:any
  @Input() status:any
  ngOnInit(): void {
  }

}
