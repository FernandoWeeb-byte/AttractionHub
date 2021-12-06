import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppRoutingModule } from '../../app-routing.module';
import {MatButtonToggleModule} from '@angular/material/button-toggle'; 
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import {MatIconModule} from '@angular/material/icon'
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import {MatSelectModule} from '@angular/material/select'; 


import { MyListComponent } from '../my-list/my-list.component';
import { AttractionComponent } from '../attraction/attraction.component';
import { AttractionItemComponent } from '../attraction-item/attraction-item.component';
import { ProfileComponent } from '../profile/profile.component';
import { HeaderLoggedComponent } from '../../header-logged/header-logged.component';
import { AttractionInfoComponent } from '../attraction-info/attraction-info.component';


@NgModule({
  declarations: [
    MyListComponent,
    AttractionItemComponent,
    ProfileComponent,
    AttractionComponent,
    HeaderLoggedComponent,
    AttractionInfoComponent
  ],
  imports: [
    CommonModule,
    AppRoutingModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatDividerModule,
    MatIconModule,
    FontAwesomeModule,
    MatSelectModule

  ],
  exports:[
    HeaderLoggedComponent,
    AttractionComponent
  ],
  schemas:[]
})
export class UserModule { }
