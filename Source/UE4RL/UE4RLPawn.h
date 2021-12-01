// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Pawn.h"
#include "GenericTeamAgentInterface.h"

#include "UE4RLPawn.generated.h"

UCLASS()
class UE4RL_API AUE4RLPawn : public APawn, public IGenericTeamAgentInterface
{
	GENERATED_BODY()

public:
	// Sets default values for this pawn's properties
	AUE4RLPawn();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	virtual FGenericTeamId GetGenericTeamId() const { return FGenericTeamId(TeamId); }

	// Our pawn is hostile towards everybody
	virtual ETeamAttitude::Type GetTeamAttitudeTowards(const AActor& Other) const override
	{
		return ETeamAttitude::Hostile;
	}

public:
	UPROPERTY(EditAnywhere, Category = Team)
	uint8 TeamId;

	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

};
