import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CadastroTelaComponent } from './cadastro-tela.component';

describe('CadastroTelaComponent', () => {
  let component: CadastroTelaComponent;
  let fixture: ComponentFixture<CadastroTelaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CadastroTelaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CadastroTelaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
