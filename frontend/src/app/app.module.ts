import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonToggleModule} from '@angular/material/button-toggle'; 
import {MatButtonModule} from '@angular/material/button';
import {MatDividerModule} from '@angular/material/divider';
import { ReactiveFormsModule } from '@angular/forms';


import {CadastroLoginModule} from './cadastro-login/cadastro-login.module';
import { UserModule } from './user/user/user.module';
import { HomeComponent } from './home/home.component';
import { SearchComponent } from './search/search.component';





@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    SearchComponent,
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    CadastroLoginModule,
    UserModule,
    ReactiveFormsModule,
    MatButtonToggleModule,
    HttpClientModule,
    MatButtonModule,
    MatDividerModule
  ],
  exports:[
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
