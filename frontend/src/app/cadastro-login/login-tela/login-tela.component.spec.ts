import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginTelaComponent } from './login-tela.component';

describe('LoginTelaComponent', () => {
  let component: LoginTelaComponent;
  let fixture: ComponentFixture<LoginTelaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LoginTelaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginTelaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
